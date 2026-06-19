import type { Policies } from "@/types/policies";


export interface AuthContextType {
    user: User | null;
    token: string | null;
    login: (userData: User, authToken: string) => void;
    logout: () => void;
}

export interface User {
    name: string,
    email: string,
    policies: Array<Policies>
}