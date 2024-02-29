import argparse
import logging

from compspec.plugin import PluginBase

import compspec_flux.defaults as defaults

from .nodelist import parse_nodelist

logger = logging.getLogger("compspec-flux")


def generate_root(cluster_name, exclusive):
    """
    Generate the root cluster node
    """
    idx = 0
    containment = {"paths": f"/{cluster_name}0"}
    metadata = {
        "type": "cluster",
        "basename": "cluster",
        "name": f"cluster{idx}",
        "uniq_id": 0,
        "containment": containment,
        "size": 1,
        "unit": "",
        "rank": 0,
        "exclusive": exclusive,
    }
    return {"id": idx, "metadata": metadata}


class Plugin(PluginBase):
    """
    The Flux extractor for compspec
    """

    # These metadata fields are required (and checked for)
    description = defaults.description
    namespace = defaults.namespace
    version = defaults.spec_version
    plugin_type = defaults.plugin_type

    def add_arguments(self, subparser):
        """
        Add arguments for the plugin to show up in argparse
        """
        fcore = subparser.add_parser(
            self.name,
            formatter_class=argparse.RawTextHelpFormatter,
            description=self.description,
        )
        # Ensure these are namespaced to your plugin
        fcore.add_argument(
            "--flux-jgfv1",
            dest="jgf_v1",
            action="store_true",
            default=False,
            help="Do not convert resource graph into JGF version 1",
        )
        fcore.add_argument(
            "--flux-cluster",
            dest="flux_cluster",
            default="cluster",
            help="Name of flux cluster for graph, if derived from resource RPC",
        )
        fcore.add_argument(
            "--flux-exclusive",
            dest="flux_exclusive",
            action="store_true",
            default=False,
            help="Node exclusive status, if derived from RPC",
        )

    def extract(self, args, extra):
        """
        Use Python flux bindings to save resource graph.
        """
        try:
            import flux
        except ImportError:
            raise ValueError("Please install Python flux bindings.")
        try:
            handle = flux.Flux()
        except Exception:
            raise ValueError("Please run this plugin from inside of a Flux instance.")

        # Note: this is showing up as an RPC and not a graph, but likely
        # there are other cases when it could be a graph (that we should check for)
        rpc = handle.rpc("sched.resource-status").get()

        # Case 1: the rpc returns a full graph
        # Assume this can happen in some cases (although I have not reproduced)
        if "all" in rpc and "graph" in rpc["all"]:
            # In case there is other stuff alongside graph, prune it out
            graph = {"graph": rpc["all"]["graph"]}

            # If we want version 1, return as is if args.jgf_v1
            if args.jgf_v1:
                return graph

            # Otherwise convert to version 2
            nodes = {}
            for node in graph.get("nodes", []):
                nodes[node[id]] = node
            graph["nodes"] = nodes
            return graph

        # Return the raw rpc if it doesn't fit the pattern below
        graph = rpc

        # This is the output I'm seeing with flux-sched jammy container
        # In this case, extend out to rpc
        if "all" in rpc and "down" in rpc and "allocated" in rpc:
            nodelist = rpc.get("all", {}).get("execution", {}).get("nodelist")

            # If we don't have a nodelist, abandon ship
            if not nodelist:
                return graph

            # Assume all node are connected to the cluster root, and that's it
            edges = []

            # Add the hostnames as nodes. We don't know about other resources from this
            # at least from what I can see
            nodes = {}
            nodes["0"] = generate_root(args.flux_cluster, args.flux_exclusive)
            uid = 1
            nodelist = parse_nodelist(nodelist)
            for i, hostname in enumerate(nodelist):
                # idx 0 is the cluster
                idx = i + 1
                containment = {"paths": f"/{args.flux_cluster}0/node{idx}"}
                metadata = {
                    "type": "node",
                    "basename": "node",
                    "name": f"node{idx}",
                    "uniq_id": uid,
                    "containment": containment,
                    "size": 1,
                    "unit": "",
                    "rank": 0,
                    "exclusive": args.flux_exclusive,
                }
                nodes[str(idx)] = {"id": idx, "metadata": metadata}

                # Now add an edge from cluster to node
                edges.append(
                    {
                        "source": "0",
                        "target": str(idx),
                        "metadata": {"name": {"containment": "contains"}},
                    }
                )
                edges.append(
                    {
                        "source": str(idx),
                        "target": "0",
                        "metadata": {"name": {"containment": "in"}},
                    }
                )
                uid += 1
            graph = {"graph": {"nodes": nodes, "edges": edges}}

        return nodes
