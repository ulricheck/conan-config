import os

from conans import tools


def pre_package_info(output, conanfile, reference, **kwargs):
    assert conanfile
    # Find bin, lib and prefix paths
    bin_paths = []
    lib_paths = []
    prefix_paths = []
    for pkg_name, cpp_info in conanfile.deps_cpp_info.dependencies:
        prefix_paths.append(cpp_info.rootpath)
        lib_path = os.path.join(cpp_info.rootpath, "lib")
        if os.path.isdir(lib_path):
            lib_paths.append(lib_path)
        bin_path = os.path.join(cpp_info.rootpath, "bin")
        if os.path.isdir(bin_path):
            bin_paths.append(bin_path)

    # Set PATH, LD_LIBRARY_PATH and CMAKE_PREFIX_PATH env vars
    for bin_path in bin_paths:
        conanfile.env_info.PATH.append(bin_path)
    for lib_path in lib_paths:
        conanfile.env_info.LD_LIBRARY_PATH.append(lib_path)
    for prefix_path in prefix_paths:
        conanfile.env_info.CMAKE_PREFIX_PATH.append(prefix_path)
