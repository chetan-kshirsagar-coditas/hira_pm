import Modal from "@/components/Modal/Modal"
import { useForm } from "react-hook-form"
import { ZOrganizationSchema, type AddOrganizationPageProps, type OrganizationData } from "./AddOrganizationPage.types"
import { snack } from "@/components/Snackbar/useSnackbarStore";
import FormInput from "@/components/Form/FormInput/FormInput";
import { MultiClass } from "@/utility/classResolve";
import styles from "./AddOrganizationPage.module.scss";
import Button from "@/components/Button/Button";
import FormSelect from "@/components/Form/FormSelect/FormSelect";
import { useCreateOrganizationMutation, useGetOrganizationQuery, useUpdateOrganizationMutation } from "@/redux/slices/orgApiSlice";
import { useEffect } from "react";
import { SubscriptionOptions } from "./constants/SubscriptionOptions";
import Form from "@/components/Form/Form";
import { zodResolver } from "@hookform/resolvers/zod";



const AddOrganizationPage = ({ id, onClose }: AddOrganizationPageProps) => {

    const isEditingMode = Boolean(id);

    const { data: organizationData, isFetching, isLoading: isFetchingData } = useGetOrganizationQuery(id || "", {
        skip: !id,
    });

    const [createOrganization, { isLoading: isCreating }] = useCreateOrganizationMutation();
    const [updateOrganization, { isLoading: isUpdating }] = useUpdateOrganizationMutation();

    const isSubmitting = isCreating || isUpdating;
    const isLoadingForm = isFetching || isFetchingData;


    const methods = useForm<OrganizationData>({
        defaultValues: {
            organization_name: "",
            org_admin_name: "",
            org_admin_email: "",
            subscription_name: "BASIC",
        },
        resolver: zodResolver(ZOrganizationSchema)
    });

    useEffect(() => {
        if (isEditingMode && organizationData) {
            methods.reset({
                organization_name: organizationData.organization_name || "",
                org_admin_name: organizationData.org_admin_name || "",
                org_admin_email: organizationData.org_admin_email || "",
                subscription_name: organizationData.subscription_name || "BASIC",
            });
        }
    }, [isEditingMode, organizationData, methods]);


    const onSubmit = async (orgData: OrganizationData) => {
        try {
            if (isEditingMode && id) {
                const response = await updateOrganization({ id: id, data: orgData }).unwrap();
                snack.success(response.message || "Organization updated successfully!");
            } else {
                const response = await createOrganization(orgData).unwrap();
                console.log("create org response: ", response);
                snack.success(response.message || "Organization created successfully!");
            }
            onClose();
        } catch (e: any) {
            snack.error(e?.data?.detail || e?.message || e?.error || "Something went wrong!");
            console.error("Organization submission error:", e);
        }
    }

    const submitButtonText = isSubmitting ? (isEditingMode ? "Updating..." : "Creating...") : isEditingMode ? "Update" : "Create";
    return (
        <Modal>
                <Form methods={methods} onSubmit={onSubmit} className={MultiClass([styles.form, styles.addOrgForm])}>
                    <span className={styles.formTitle}>{isEditingMode ? "Edit Organization" : "Add Organization"}</span>
                    {isLoadingForm && (
                        <div className={styles.loadingState}>
                            <p>Loading organization details...</p>
                        </div>
                    )}
                    <FormInput<OrganizationData>
                        name="organization_name"
                        placeholder="Enter organization name here..."
                        label="Organization Name"
                    />

                    <FormInput<OrganizationData>
                        name="org_admin_name"
                        placeholder="Enter organization admin name here..."
                        label="Organization Admin Name"
                    />


                    {
                        !isEditingMode && <FormInput<OrganizationData>
                            name="org_admin_email"
                            placeholder="Enter organization admin email here..."
                            label="Organization Admin Email"
                        />
                    }

                    <FormSelect<OrganizationData>
                        name="subscription_name"
                        label="Subscription Type"
                        options={SubscriptionOptions}
                    />

                    <div className={styles.formButtonsContainer}>
                        <Button
                            variant="primary"
                            type="submit"
                            disabled={isSubmitting || isLoadingForm}
                        >
                            {submitButtonText}
                        </Button>
                        <Button
                            onClick={onClose}
                            type="button"
                            disabled={isSubmitting}
                        >
                            Cancel
                        </Button>
                    </div>
                </Form>
        </Modal >
    )
}

export default AddOrganizationPage