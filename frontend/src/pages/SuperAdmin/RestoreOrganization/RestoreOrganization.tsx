import Button from "@/components/Button/Button"
import Modal from "@/components/Modal/Modal"
import styles from "./RestoreOrganization.module.scss";
import { useRestoreOrganizationMutation } from "@/redux/slices/orgApiSlice";
import { snack } from "@/components/Snackbar/useSnackbarStore";
import type { RestoreOrganizationProps } from "./RestoreOrganization.types";
import Typography from "@/components/Typography/Typography";

const RestoreOrganization = ({ id, onClose }: RestoreOrganizationProps) => {
    const [restoreOrganization, { isLoading: isRestoring }] = useRestoreOrganizationMutation();
    const onDelete = async () => {
        try {
            const response = await restoreOrganization(id ? id : "").unwrap();
            snack.success(response.message || "Organization archived successfully!");
            onClose();
        } catch (e: any) {
            snack.error(e?.data?.detail || e?.message || "Something went wrong!");
            console.error("Organization deletion error:", e);
        }
    }
    return (
        <Modal>
            <div>
                <Typography variant="label">Are you sure you want restore?</Typography>
                <div className={styles.btnContainer}>
                    <Button variant="primary" onClick={onDelete}>{isRestoring ? "Restoring..." : "Restore"}</Button>
                    <Button onClick={onClose}>Cancel</Button>
                </div>
            </div>
        </Modal>
    )
}

export default RestoreOrganization