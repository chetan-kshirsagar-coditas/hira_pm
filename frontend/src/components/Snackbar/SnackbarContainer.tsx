import { v4 } from "uuid";
import { useSnackstore } from "./useSnackbarStore"
import styles from "./SnackbarContainer.module.scss";
const SnackbarContainer = () => {
  const snaps = useSnackstore();
  return (
    <div className={styles.snackbarContainer}>
      {
        snaps.map(s => <span key={v4()} className={s.type === "error" ? styles.error : styles.success}>{s.message}</span>)
      }
    </div>
  )
}

export default SnackbarContainer