# Conan config
This repository contains all the shared conan configuration.

Install: `conan config install git@gitlab.com:aivero/public/conan/conan-config.git`

## Overview:
- `conan.conf`: Global configuration for Conan.
- `remotes.txt`: Configuration for Conan repositories.
- `settings.yml`: Collection of all possible Conan settings. E.g build_type, os, compiler
- `profiles`: Configuration for specific setups.
- `hooks`: Configuration scripts that run before or after Conan methods.
