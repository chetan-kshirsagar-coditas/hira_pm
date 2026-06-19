import { lazy } from "react";
import { createBrowserRouter } from "react-router-dom";
import GUARDS from "./guards";
import ArchivedOrganizations from "@/pages/SuperAdmin/ArchivedOrganizations/ArchivedOrganizations";
import AppLayout from "@/layouts/AppLayout/AppLayout";
const SetPasswordPage = lazy(() => import("@/pages/SetPasswordPage/SetPasswordPage"));
const UnauthorizedPage = lazy(() => import("@/pages/UnauthorizedPage/UnauthorizedPage"));
const Dashboard = lazy(() => import("@/pages/SuperAdmin/Dashboard/Dashboard"));
const OrganizationsPage = lazy(() => import("@/pages/SuperAdmin/OrganizationsPage/OrganizationsPage"));
const App = lazy(() => import("../App"));
const LandingPage = lazy(() => import("@/pages/LandingPage/LandingPage"));

type Predicate = () => boolean;

const canActive = (component: React.ComponentType, guards: Predicate[]) => {
    if (guards.every(guard => guard())) {
        return component;
    }
    return UnauthorizedPage;
}

export const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                path: "",
                element: <LandingPage />
            },
            {
                path: "dashboard",
                Component: canActive(AppLayout, [GUARDS.isLoggedIn]),
                children: [
                    {
                        path: "metrics",
                        element: <Dashboard />
                    },
                    {
                        path: "organizations",
                        element: <OrganizationsPage />,
                    },
                    {
                        path: "organizations/archived",
                        element: <ArchivedOrganizations />,
                    },
                ]
            },
            {
                path: "/auth/org_admin_set_password",
                element: <SetPasswordPage />
            }
        ]
    }
])



