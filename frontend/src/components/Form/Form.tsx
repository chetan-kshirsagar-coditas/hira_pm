import { FormProvider } from "react-hook-form"
import type { FormProps } from "./Form.types"


const Form = ({ children, methods, onSubmit, className }: FormProps) => {
    return (
        <FormProvider {...methods}>
            <form onSubmit={methods.handleSubmit(onSubmit)} className={className ?? ""}>{children}</form>
        </FormProvider>
    )
}

export default Form