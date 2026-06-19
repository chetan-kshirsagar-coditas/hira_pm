import type { FormFieldProps } from "./FormField.types";
import styles from "./FormField.module.scss";
const FormField = ({ children, label, error, required }: FormFieldProps) => {
    return (
        <div className={styles.formField}>
            <label htmlFor="">{label} {required && <span className={styles.asterisk}>*</span>}</label>
            {children}
            {error && <span className={styles.validationErrorMsg}>{error}</span>}
        </div>
    )
}

export default FormField