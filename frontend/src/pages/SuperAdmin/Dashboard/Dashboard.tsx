import DashboardCard from "./components/DashboardCard/DashboardCard"
import styles from "./Dashboard.module.scss";
const Dashboard = () => {
  return (
    <div className={styles.dashboard}>
      <DashboardCard count={3} text="Active Organizations"/>
      <DashboardCard count={23} text="Active Users"/>
    </div>
  )
}

export default Dashboard