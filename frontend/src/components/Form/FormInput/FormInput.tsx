import { Controller, useFormContext, type FieldValues } from "react-hook-form"
import type { FormInputProps } from "./FormInput.types"
import FormField from "../FormField/FormField"
import styles from "./FormInput.module.scss";


const FormInput = <T extends FieldValues>({ name, label, placeholder, rules, type }: FormInputProps<T>) => {
    const { control } = useFormContext<T>();
    return (
        <div>
            <Controller
                name={name}
                control={control}
                rules={rules}
                render={({ field, fieldState: { error } }) =>
                    <FormField
                        label={label}
                        required={!!rules?.required}
                        error={error?.message}
                    >
                        <input
                            className={styles.formInput}
                            {...field}
                            id={name}
                            placeholder={placeholder}
                            type={type}
                        />
                    </FormField>
                }
            />
        </div>
    )
}

export default FormInput