import styles from "./Navbar.module.scss";
const Navbar = () => {
  return (
    <header className={styles.header}>
      <span className={styles.Hira}>HIRA</span>
      <nav className={styles.navbar}>
        <div>
          <span>features</span>
          <span>guide</span>
          <span>pricing</span>
          <span>solutions</span>
        </div>
      </nav>
    </header>
  )
}

export default Navbar