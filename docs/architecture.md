# Template structure

The root is a working Python package used to maintain and test the template. `template/` contains the files Copier writes into a new project. `copier.yml` defines the questions and name validation.

Changes to shared tooling usually need to be made in both places. Integration tests generate a project with non-default names and check Copier updates. CI separately runs the generated project's checks and builds its wheel.

The template provides a development baseline. Applications, deployments and security controls specific to a service belong in the generated project.
