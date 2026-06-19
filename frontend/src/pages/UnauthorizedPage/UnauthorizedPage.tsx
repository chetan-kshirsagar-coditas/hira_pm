import Typography from "@/components/Typography/Typography";
import styles from "./UnauthorizedPage.module.scss";
import Button from "@/components/Button/Button";
import { useNavigate } from "react-router-dom";

const UnauthorizedPage = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.unauthorizedPage}>
      <div className={styles.displayUnauthorized}>
        <Typography variant="h2"><i className="fa-solid fa-triangle-exclamation"></i>  Unauthorized Acess </Typography>
        <Button onClick={() => navigate("/")}>Go Back</Button>
      </div>
    </div>
  )
}


export default UnauthorizedPage