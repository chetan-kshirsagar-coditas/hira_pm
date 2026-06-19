import Typography from "@/components/Typography/Typography"
import styles from "./HeroSection.module.scss"

const HeroSection = () => {
    return (
        <>
            <p className={styles.heroText}>
                <span>More projects.</span>
                <span>More Agents.</span>
                <span>Less chaos.</span>
            </p>
            <p className={styles.heroDescription}>
                <Typography variant="caption">Hira orchestrates across your AI tech stack
                    turning plans into actions and shipped work.</Typography>
            </p>
        </>
    )
}

export default HeroSection