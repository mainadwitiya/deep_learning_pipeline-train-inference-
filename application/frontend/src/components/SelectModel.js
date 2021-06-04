import React, { Component } from "react";
import "./SelectModel.css";

export default class SelectModel extends Component {
  render() {
    return (
      <div>
        <div className="dropdown">
          <button className="dropbtn">Select Model Type</button>
          <div className="dropdown-content">
            <div className="classificationDropdown">
              <a href="#">Classification</a>
              <div className="classificationContent">
                <a href="/model/keras">1. Keras</a>
                <a href="#">2. Scikit</a>
                <a href="#">2. Pytorch</a>
              </div>
            </div>
            <div className="od-dropdown">
              <a href="#">Object Detection</a>
              <div className="ODContent">
                <a href="/model/tensorflow">1. Tensorflow</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
