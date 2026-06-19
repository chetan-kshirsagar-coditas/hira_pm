import Button from "@/components/Button/Button"
import Modal from "@/components/Modal/Modal"
import styles from "./DeleteOrganization.module.scss";
import { useDeleteOrganizationMutation } from "@/redux/slices/orgApiSlice";
import { snack } from "@/components/Snackbar/useSnackbarStore";
import type { DeleteOrganizationProps } from "./DeleteOrganization.types";
import Typography from "@/components/Typography/Typography";

const DeleteOrganization = ({ id, onClose }: DeleteOrganizationProps) => {

    const [deleteOrganization, { isLoading: isDeleting }] = useDeleteOrganizationMutation();

    const onDelete = async () => {
        try {
            const response = await deleteOrganization(id ? id : "").unwrap();
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
                <Typography variant="label">Are you sure you want delete?</Typography>
                <div className={styles.btnContainer}>
                    <Button variant="tertiary" onClick={onDelete}>{isDeleting ? "Deleting..." : "Delete"}</Button>
                    <Button onClick={onClose}>Cancel</Button>
                </div>
            </div>
        </Modal>
    )
}

export default DeleteOrganization