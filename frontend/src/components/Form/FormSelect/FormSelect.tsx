import { Controller, useFormContext, type FieldValues } from "react-hook-form"
import FormField from "../FormField/FormField"
import styles from "./FormSelect.module.scss";
import type { FormSelectProps } from "./FormSelect.types";


const FormSelect = <T extends FieldValues>({ name, label, options, rules }: FormSelectProps<T>) => {
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
                        <select id={name} {...field} className={styles.formSelect}>
                            {
                                options.map(option => <option value={option.value} key={option.value}>{option.label}</option>)
                            }
                        </select>
                    </FormField>
                }
            />
        </div>
    )
}

export default FormSelect