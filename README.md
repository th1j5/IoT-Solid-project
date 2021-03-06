# IoT-Solid-project

Project to assemble all repo's partaining to the IoT Solid project with LwM2M for Cross-Course Project at Ghent University (2019-2020).

---

Thijs Paelman - [thijs.paelman@ugent.be](mailto:thijs.paelman@ugent.be)

Flor Sanders - [flor.sanders@ugent.be](mailto:flor.sanders@ugent.be)

Axl Bomhals - [axl.bomhals@ugent.be](mailto:axl.bomhals@ugent.be)

Kobe Hens - [kobe.hens@ugent.be](mailto:kobe.hens@ugent.be)

---

The complete system is visualized in the network diagram below. The different components can be found in the submodules included in this repository.
All technical details about the system are described in the [report](./report/Report.pdf).

![proof-of-concept-1](README.assets/proof-of-concept-1.png)

Remember, we are using submodules, so after cloning this repository, execute:
```
git submodule init
git submodule update <name-of-module>
# for each submodule, because otherwise you get credentials asked in random order (and through each other)
```


See subrepositories for details on installation, dependencies, functionality and usage.

For Leshan there is choice:
 - The leshan-server-solid is an effort to make a standalone Leshan server project using maven/git, while depending on the Leshan project.
 - However, the leshan-server-demo in Leshan has now incorporated our code, thus no difference exist in functionality, except that the demo server is upstream and will receive updates (and maybe breaking changes)
