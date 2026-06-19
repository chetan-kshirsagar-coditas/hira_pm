import { MultiClass } from "@/utility/classResolve";
import Navbar from "../../components/Navbar/Navbar";
import LoginPage from "../LoginPage/LoginPage";
import HeroSection from "./components/HeroSection/HeroSection";
import styles from "./LandingPage.module.scss";

const LandingPage = () => {
    return (
        <>
            <Navbar />
            <div className={styles.landingPage}>
                <div className={MultiClass([styles.landingPageSection, styles.leftSection])}>
                    <HeroSection/>
                </div>
                <div className={MultiClass([styles.landingPageSection, styles.rightSection])}>
                    <LoginPage />
                </div>
            </div>
        </>
    )
}

export default LandingPage