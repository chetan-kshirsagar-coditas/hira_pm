import { useSyncExternalStore } from "react";
import { v4 } from "uuid";

type SnackType = "success" | "error";

interface SnackItem {
    id: string,
    type: SnackType,
    message: string
}

type Listener = () => void;

const listerners = new Set<Listener>();

let snapshot: SnackItem[] = [];

const subscribe = (listener: Listener) => {
    listerners.add(listener);
    return () => listerners.delete(listener);
}

const getSnapshot = (): SnackItem[] => snapshot;

const notify = () => {
    snapshot = [...snapshot];
    listerners.forEach(listener => listener());
}

export const snack = (message: string, type: SnackType = "success") => {
    const id = v4();
    snapshot = [...snapshot, { id, message, type } ];
    notify();

    setTimeout(() => {
        snapshot = snapshot.filter(snap => snap.id !== id);
        notify();
    }, 3000);
}

snack.success = (message: string) => snack(message, "success");
snack.error = (message: string) => snack(message, "error");


export const useSnackstore: () => SnackItem[] = () => useSyncExternalStore(subscribe, getSnapshot, getSnapshot); 