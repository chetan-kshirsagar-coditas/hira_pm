import type { ButtonHTMLAttributes } from "react";

type Variant = "primary" | "secondary" | "tertiary" | "outline-secondary" | "outline-tertiary" | "outline-success"

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: Variant
}