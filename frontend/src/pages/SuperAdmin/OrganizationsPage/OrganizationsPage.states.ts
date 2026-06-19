import type { ModalAction, ModalState } from "./OrganizationsPage.types";

export const modalReducer = (state: ModalState, action: ModalAction): ModalState => {

  if (!action) return null;

  switch (action.type) {

    case "ADD_ORGANIZATION":
      return {
        type: "ADD_ORGANIZATION"
      }

    case "UPDATE_ORGANIZATION":
      return {
        type: "UPDATE_ORGANIZATION",
        id: action.id
      }

    case "DELETE_ORGANIZATION":
      return {
        type: "DELETE_ORGANIZATION",
        id: action.id
      }

    default:
      return state
  }
}