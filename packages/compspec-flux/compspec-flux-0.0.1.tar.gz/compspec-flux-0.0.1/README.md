# Compspec Flux

<p align="center">
  <img height="300" src="https://raw.githubusercontent.com/compspec/spec/main/img/compspec-circle.png">
</p>

[![PyPI version](https://badge.fury.io/py/compspec-flux.svg)](https://badge.fury.io/py/compspec-flux)

A compspec (Composition spec) is a specification and model for comparing things. Compspec Flux
provides a simple means to extract metadata about a running flux instance, namely the graph of nodes.
Other links of interest include:

 - [Compspec](https://github.com/compspec/compspec): the Python library that discovers and loads this plugin.
 - [Compatibility](https://github.com/compspec/spec/tree/main/compatibility): of container images and applications to a host environment.
 - [Compspec Go](https://github.com/compspec/compspec-go): the Go library that retrieves artifacts and makes graphs for image selection and scheduling.

## Usage

Install compspec and the plugin here:

```bash
pip install compspec
pip install compspec-flux
```

Then (alongside a Flux instance) run the plugin. Note that the VSCode setup [provided here](.devcontainer) will provide this for you.
You can use defaults, or add any parameters to the plugin after the plugin name "flux" Here is how to start a flux instance:

```bash
flux start --test-size=4
```

And here is how to print to the terminal:

```bash
compspec extract flux
```

<details>

<summary>Flux output</summary>

```console
{
    "0": {
        "id": 0,
        "metadata": {
            "type": "cluster",
            "basename": "cluster",
            "name": "cluster0",
            "uniq_id": 0,
            "containment": {
                "paths": "/cluster0"
            },
            "size": 1,
            "unit": "",
            "rank": 0,
            "exclusive": false
        }
    },
    "1": {
        "id": 1,
        "metadata": {
            "type": "node",
            "basename": "node",
            "name": "node1",
            "uniq_id": 1,
            "containment": {
                "paths": "/cluster0/node1"
            },
            "size": 1,
            "unit": "",
            "rank": 0,
            "exclusive": false
        }
    }
}
```

</details>

And how to save to file

```bash
compspec extract --outfile cluster-resources.json flux
```


## License

HPCIC DevTools is distributed under the terms of the MIT license.
All new contributions must be made under this license.

See [LICENSE](https://github.com/converged-computing/cloud-select/blob/main/LICENSE),
[COPYRIGHT](https://github.com/converged-computing/cloud-select/blob/main/COPYRIGHT), and
[NOTICE](https://github.com/converged-computing/cloud-select/blob/main/NOTICE) for details.

SPDX-License-Identifier: (MIT)

LLNL-CODE- 842614
