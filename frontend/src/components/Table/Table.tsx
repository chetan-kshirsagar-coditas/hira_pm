import { MultiClass } from "@/utility/classResolve";
import styles from "./Table.module.scss";
import type { TableBodyProps, TableCellProps, TableHeadCellProps, TableHeadProps, TableProps, TableRowProps } from "./Table.types";
const Table = ({ children }: TableProps) => {
    return (
        <table className={styles.table}>{children}</table>
    )
}

Table.TableHead = ({ children, className }: TableHeadProps) => <thead className={MultiClass([styles.tableHead, className ? className: ""])}>{children}</thead>;
Table.TableBody = ({ children, className }: TableBodyProps) => <tbody className={className ? className: ""}>{children}</tbody>;
Table.TableRow = ({ children, className }: TableRowProps) => <tr className={className ? className: ""}>{children}</tr>;
Table.TableHeadCell = ({ children, className }: TableHeadCellProps) => <th className={MultiClass([styles.tableHeadCell, className ? className: ""])}>{children}</th>;
Table.TableCell = ({ children, className }: TableCellProps) => <td className={MultiClass([styles.tableCell, className ? className: ""])}>{children}</td>;


export default Table