// Typography.types.ts
import type { PropsWithChildren } from "react"

export type TypoVariant =
    "h1" |
    "h2" |
    "h3" |
    "caption" |
    "body1" |
    "label" 

export interface TypographyProps extends PropsWithChildren {
    variant: TypoVariant
}