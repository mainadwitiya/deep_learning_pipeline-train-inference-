import { Fragment, useState } from "react";
import { Route } from "react-router";
// import { Link } from "react-router-dom";
import axios from "axios";
import ModelForm from "../components/model/ModelForm";

const Model = () => {
  // const location = useLocation();
  const [data, setData] = useState({
    usecase_type: "object-detection", //object-detection / classification
    framework_type: "tensorflow", // tensorflow, keras, pytorch
    model_arch_type: "", // resnet, fasterRcnn
    training_file: "",
    validation_file: "",
    label_file: "",
  });

  const archChangeHandler = (e) => {
    setData({ ...data, model_arch_type: e.target.value });
    // console.log(e.target.value);
  };

  const trainingFileHandler = (e) => {
    setData({ ...data, training_file: e.target.files[0] });
  };

  const validationFileHandler = (e) => {
    setData({ ...data, validation_file: e.target.files[0] });
  };

  const labelFileHandler = (e) => {
    setData({ ...data, label_file: e.target.files[0] });
  };

  const submitDataHandler = (e) => {
    e.preventDefault();

    let form_data = new FormData();
    form_data.append("training_data", data.training_file);
    form_data.append("test_data", data.validation_file);
    form_data.append("label_file_data", data.label_file);
    form_data.append("model_arch_type", data.model_arch_type);
    form_data.append("usecase_type", data.usecase_type);
    form_data.append("framework_type", data.framework_type);

    let url = "http://127.0.0.1:8000/apis/model_records/";

    axios
      .post(url, form_data, {
        headers: {
          "content-type": "multipart/form-data",
        },
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  console.log(data);
  return (
    <Fragment>
      <div className="container">
        <h4 className="text-center mt-4">File Upload Page.</h4>
        <div className="row">
          <div className="col-6 offset-3">
            {/* Model Form Component */}
            <ModelForm
              onUploadTrainingFile={trainingFileHandler}
              onUploadValidationFile={validationFileHandler}
              onUploadLabelFile={labelFileHandler}
            />
            <Route path={"/model/tensorflow/select-arch"}>
              <div className="card mt-4">
                <div className="card-header">
                  <h4 className="text-left mb-0">TF Architecture</h4>
                </div>
                <div className="card-body">
                  <h6 className="text-left text-uppercase">
                    Select Architecture
                  </h6>

                  <div className="row">
                    <div className="col-6">
                      <div className="input-group">
                        <div className="input-group-prepend">
                          <div className="input-group-text">
                            <input
                              type="radio"
                              name="architecture"
                              className="architecture"
                              value="fasterrcnn"
                              onClick={archChangeHandler}
                              aria-label="Radio button for following text input"
                            />
                          </div>
                        </div>
                        <div className="form-control">Fasterrcnn</div>
                      </div>
                    </div>
                    <div className="col-6">
                      <div className="input-group">
                        <div className="input-group-prepend">
                          <div className="input-group-text">
                            <input
                              type="radio"
                              name="architecture"
                              className="architecture"
                              value="centernet"
                              onClick={archChangeHandler}
                              aria-label="Radio button for following text input"
                            />
                          </div>
                        </div>
                        <div className="form-control">Centernet</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </Route>
            <div className="text-right mt-4">
              {/* <Link
                  to={`/architecture?arch=${data.arch_type}`}
                  className="btn btn-primary px-4"
                >
                  proceed
                </Link> */}
              <button
                onClick={submitDataHandler}
                className="btn btn-primary px-4"
                type="submit"
              >
                submit
              </button>
            </div>
          </div>
        </div>
      </div>
    </Fragment>
  );
};

export default Model;
