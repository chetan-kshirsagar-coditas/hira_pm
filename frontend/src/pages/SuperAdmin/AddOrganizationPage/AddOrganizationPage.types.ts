import z from "zod";

export const ZOrganizationSchema = z.object({
    organization_id: z.string().optional(),
    organization_name: z.string().trim().nonempty("Organization name is required."),
    org_admin_name: z.string().trim().nonempty("Organization admin name is required."),
    org_admin_email: z.email("Invalid email").nonempty("Organization admin email is required."),
    subscription_name: z.enum(["BASIC", "HALF", "FULL"])
})

export type OrganizationData = z.infer<typeof ZOrganizationSchema>;

export interface AddOrganizationPageProps {
    id?: string,
    onClose: () => void
}


 
