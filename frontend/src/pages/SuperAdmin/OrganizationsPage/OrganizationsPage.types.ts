
type ActionType = "ADD_ORGANIZATION" | "UPDATE_ORGANIZATION" | "DELETE_ORGANIZATION";

export type ModalState =
    { type: ActionType, id?: string } | null

export type ModalAction =
    { type: "ADD_ORGANIZATION" } |
    { type: ActionType, id: string } |
    { type: ActionType, id: string } |
    null