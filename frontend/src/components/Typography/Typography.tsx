import styles from "./Typography.module.scss";
import type { TypographyProps } from "./Typography.types";
const Typography = ({ children, variant}: TypographyProps) => {
    
        switch(variant){
            case "h1":
                return <h1 className={styles[variant]}>{children}</h1>
            case "h2":
                return <h1 className={styles[variant]}>{children}</h1>
            case "h3":
                return <h1 className={styles[variant]}>{children}</h1>
            case "caption":
                return <span className={styles[variant]}>{children}</span>
            case "label":
                return <label className={styles[variant]}>{children}</label>

        }
    
}

export default Typography