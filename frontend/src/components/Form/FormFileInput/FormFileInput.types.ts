import type { FieldValues, RegisterOptions, Path } from "react-hook-form";
import type { BaseFieldProps } from "../Form.types";

export interface FormFileInputProps<T extends FieldValues> extends BaseFieldProps<T> {
    accept?: string
    placeholder?: string,
    rules?: RegisterOptions<T, Path<T>>
}