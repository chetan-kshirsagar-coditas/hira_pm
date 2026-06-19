import styles from "./DashboardCard.module.scss";
import type { DashboardCardProps } from "./DashboardCard.types";

const DashboardCard = ({ count, text }: DashboardCardProps) => {
  return (
    <div className={styles.dashboardCard}>
        <div className={styles.counter}>
            <span>{count}</span>
        </div>
        <div>
            {text}
        </div>
    </div>
  )
}

export default DashboardCard