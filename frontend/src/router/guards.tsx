// import { useAuth } from "@/context/AuthContext";
import type { User } from "@/context/types"
import type { Policies } from "@/types/policies";

// export function Guards() {
//     const { user } = useAuth();
//     const isLoggedIn = (): boolean => {
//         return !!user;
//     };

//     const hasAccess = (allowed: Array<Policies>): boolean => {
//         if (!user || !user.policies) return false;
//         return user.policies.every(policy => allowed.includes(policy));
//     };

//     return { isLoggedIn, hasAccess };
// }


const isLoggedIn = () => {
    const user = localStorage.getItem("user");
    return !!user;
}

const hasAccess = (allowed: Array<Policies>): boolean => {
    const user: User = JSON.parse(localStorage.getItem("user")!);
        if (!user || !user.policies) return false;
        return user.policies.every(policy => allowed.includes(policy));
    };



export default {
    isLoggedIn,
    hasAccess
}