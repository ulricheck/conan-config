def pre_export(output, conanfile, conanfile_path, reference, **kwargs):
    # Add warning if license and description is missing
    for field in ["license", "description"]:
        field_value = getattr(conanfile, field, None)
        if not field_value:
            output.warn("Conanfile doesn't have '%s'. It is recommended to add it as attribute"
                        % field)
