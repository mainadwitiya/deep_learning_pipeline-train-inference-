import "./App.css";
import React, { Component } from "react";

export default class connectionExample extends Component {
  componentDidMount() {
    const apiUrl = "https://127.0.0.1:8000/models/";
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => console.log(data));
  }
  render() {
    return <div>Sample connection banaya hai</div>;
  }
}
