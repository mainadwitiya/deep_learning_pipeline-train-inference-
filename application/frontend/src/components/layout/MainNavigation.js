import { Fragment } from "react";
import { Link } from "react-router-dom";

const MainNavigation = () => {
  return (
    <Fragment>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <Link to="/" className="nav-link font-weight-bold">
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/model" className="nav-link font-weight-bold">
                Model
              </Link>
            </li>
          </ul>
        </div>
      </nav>
    </Fragment>
  );
};

export default MainNavigation;
