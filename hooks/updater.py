import os


def pre_export(output, conanfile, conanfile_path, reference, **kwargs):
    os.system("conan config install https://gitlab.com/aivero/public/conan/conan-config.git")
