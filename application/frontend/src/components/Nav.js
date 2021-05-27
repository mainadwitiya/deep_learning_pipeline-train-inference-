import React, { Component } from "react";
import "./Nav.css";
import ModelPage from "./components/ModelPage";
export default class Nav extends Component {
  render() {
    return (
      <div>
        <nav>
          <ul>
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#">Models</a>
            </li>
            <li>
              <a href="#">Data</a>
            </li>
          </ul>
        </nav>
      </div>
    );
  }
}
