import { NavLink, Outlet, useNavigate } from "react-router-dom";
import Button from "@/components/Button/Button";
import Typography from "@/components/Typography/Typography";
import diamondLogo from "@/assets/diamond.png";
import { useAuth } from "@/context/AuthContext";
import styles from "./AppLayout.module.scss";
import type { NavItem } from "./AppLayout.types";



const NAV_ITEMS_BY_ROLE: Record<string, NavItem[]> = {
    SUPERADMIN: [
        { label: "Dashboard", to: "metrics" },
        { label: "Organizations", to: "organizations" },
        { label: "Archived", to: "organizations/archived" },
    ],
    ORGADMIN: [
        { label: "Taskify", to: "" },
        { label: "Tasktic", to: "" },
        { label: "Trello", to: "" },
        { label: "Proofhub", to: "" },
    ],
    PROJECT_COLLABRATOR: [
        { label: "Taskify", to: "" },
        { label: "Tasktic", to: "" },
    ],
};

const AppLayout = () => {
    const { user, logout } = useAuth();
    const navigate = useNavigate();

    const navItems = NAV_ITEMS_BY_ROLE[user?.policies[0] ?? ""] ?? [];

    return (
        <div className={styles.layoutContainer}>
            <div className={styles.leftPanel}>
                <div className={styles.hiraContainer}>
                    <img src={diamondLogo} alt="diamondLogo" />
                    <span>Hira</span>
                </div>
                <div className={styles.navContainer}>
                    {navItems.map(({ label, to }) => (
                        <NavLink key={label} to={to} className={styles.navLink}>
                            {label}
                        </NavLink>
                    ))}
                </div>
            </div>
            <div className={styles.rightPanel}>
                <div className={styles.layoutNav}>
                    <Typography variant="label">{user?.name}</Typography>
                    <Button
                        variant="tertiary"
                        onClick={() => {
                            logout();
                            navigate("/");
                        }}
                    >
                        Logout
                    </Button>
                </div>
                <Outlet />
            </div>
        </div>
    );
};

export default AppLayout;