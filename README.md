# IoT-Solid-project
Project to assemble all repo's partaining to the IoT Solid project with LwM2M for VOP.

Remember, we are using submodules, so after cloning this repository, execute:
	git submodule update --init --recursive

See subrepositories for details on installation, dependencies, functionality and usage.

For Leshan there is choice:
 - The leshan-server-solid is an effort to make a standalone Leshan server project using maven/git, while depending on the Leshan project.
 - However, the leshan-server-demo in Leshan has now incorporated our code, thus no difference exist in functionality, except that the demo server is upstream and will receive updates (and maybe breaking changes)
