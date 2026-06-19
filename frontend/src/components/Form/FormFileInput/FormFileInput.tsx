// FormFileInput.tsx
import { Controller, useFormContext,  type FieldValues} from "react-hook-form";
import styles from "./FormFileInput.module.scss";
import type { FormFileInputProps } from "./FormFileInput.types";
import FormField from "../FormField/FormField";


const FormFileInput = <T extends FieldValues>({ name, label, accept = ".pdf", rules }: FormFileInputProps<T>) => {

    const { control } = useFormContext<T>()
    return (
        <div>
            <Controller
                name={name}
                control={control}
                rules={rules}
                render={({ field: { onChange }, fieldState: { error } }) =>
                    <FormField
                        label={label}
                        error={error?.message}
                        required={!!rules?.required}
                    >
                        <input className={styles.formFileInput} type="file" accept={accept} onChange={(e) => onChange(e.target.files?.[0])} />
                    </FormField>}
            />
        </div>
    );
};

export default FormFileInput;