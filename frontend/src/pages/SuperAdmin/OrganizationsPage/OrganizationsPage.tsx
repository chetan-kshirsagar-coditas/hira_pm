import Button from "@/components/Button/Button";
import SearchBar from "@/components/SearchBar/SearchBar";
import Table from "@/components/Table/Table";
import styles from "./OrganizationsPage.module.scss";
import { Outlet } from "react-router-dom";
import { useGetOrganizationsQuery } from "@/redux/slices/orgApiSlice";
import Loader from "@/components/Loader/Loader";
import { useReducer } from "react";
import AddOrganizationPage from "../AddOrganizationPage/AddOrganizationPage";
import { modalReducer } from "./OrganizationsPage.states";
import DeleteOrganization from "../DeleteOrganization/DeleteOrganization";


const OrganizationsPage = () => {

  const [modal, setModal] = useReducer(modalReducer, null);

  const closeModal = () => setModal(null);

  const { data, isFetching } = useGetOrganizationsQuery(undefined);
  return (
    <div className={styles.organizationsPage}>
      <Outlet />

      {modal?.type === "ADD_ORGANIZATION" && <AddOrganizationPage onClose={closeModal} />}
      {modal?.type === "UPDATE_ORGANIZATION" && <AddOrganizationPage id={modal.id} onClose={closeModal} />}
      {modal?.type === "DELETE_ORGANIZATION" && <DeleteOrganization id={modal.id!} onClose={closeModal} />}

      <div className={styles.orgActionsContainer}>
        <SearchBar />
        <Button variant="primary" onClick={() => setModal({ type: "ADD_ORGANIZATION" })}>+ ADD</Button>
      </div>
      {isFetching && <Loader />}
      <Table>
        <Table.TableHead>
          <Table.TableRow>
            <Table.TableHeadCell>Organization Name</Table.TableHeadCell>
            <Table.TableHeadCell>Admin Name</Table.TableHeadCell>
            <Table.TableHeadCell>Admin Email</Table.TableHeadCell>
            <Table.TableHeadCell>Subscription Model</Table.TableHeadCell>
            <Table.TableHeadCell>Actions</Table.TableHeadCell>
          </Table.TableRow>
        </Table.TableHead>
        <Table.TableBody>
          {
            data?.map(organization => <Table.TableRow key={organization.organization_id}>
              <Table.TableCell>{organization.organization_name}</Table.TableCell>
              <Table.TableCell>{organization.org_admin_name}</Table.TableCell>
              <Table.TableCell>{organization.org_admin_email}</Table.TableCell>
              <Table.TableCell>{organization.subscription_name}</Table.TableCell>
              <Table.TableCell className={styles.actionBtnCell}>
                <Button variant="outline-secondary" onClick={() => setModal({ type: "UPDATE_ORGANIZATION", id: organization.organization_id! })}>Edit</Button>
                <Button variant="outline-tertiary" onClick={() => setModal({ type: "DELETE_ORGANIZATION", id: organization.organization_id! })}>Delete</Button>
              </Table.TableCell>
            </Table.TableRow>)
          }
        </Table.TableBody>
      </Table>
    </div>
  )
}

export default OrganizationsPage




