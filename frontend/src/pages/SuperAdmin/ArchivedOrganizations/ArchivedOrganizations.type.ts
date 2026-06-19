
type ActionType = "RESTORE_ORGANIZATION";

export type ModalState =
    { type: ActionType, id: string } | null

export type ModalAction =
    { type: ActionType, id: string } |
    null