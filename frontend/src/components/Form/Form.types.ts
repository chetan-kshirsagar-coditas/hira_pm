import type { PropsWithChildren } from "react";
import type { FieldValues, Path, UseFormReturn } from "react-hook-form";


export interface BaseFieldProps<T extends FieldValues> {
    name: Path<T>,
    label: string,
}

export interface FormProps extends PropsWithChildren {
    methods: UseFormReturn<any, any, any>,
    onSubmit: (data: any) => Promise<void>,
    className?: string 
}