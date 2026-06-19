import styles from "./SearchBar.module.scss";
const SearchBar = () => {
    return (
        <div className={styles.searchBar}>
            <i className="fa-solid fa-magnifying-glass"></i>
            <input type="text" placeholder="Search"/>
        </div>
    )
}

export default SearchBar