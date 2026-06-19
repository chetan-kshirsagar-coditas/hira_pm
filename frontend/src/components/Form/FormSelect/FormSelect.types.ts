import type { FieldValues, RegisterOptions, Path } from "react-hook-form";
import type { BaseFieldProps } from "../Form.types";

interface Option {
    label: string,
    value: string
}
export interface FormSelectProps<T extends FieldValues> extends BaseFieldProps<T> {
    options: Option[]
    rules?: RegisterOptions<T, Path<T>>
}