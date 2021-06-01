import { Fragment, useState } from "react";
import { Route, useRouteMatch } from "react-router";
import { Link } from "react-router-dom";
import ModelForm from "../components/model/ModelForm";

const Model = () => {
  const matchRte = useRouteMatch();

  const [arch, setArch] = useState("");

  const archChangeHandler = (e) => {
    setArch(e.target.value);
    console.log(e.target.value);
  };

  return (
    <Fragment>
      <div className="container">
        <h4 className="text-center mt-4">File Upload Page.</h4>
        <div className="row">
          <div className="col-6 offset-3">
            {/* Model Form Component */}
            <ModelForm />
            <Route path={`${matchRte.path}/select-arch`}>
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
                              value="Fasterrcnn"
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
                              value="Centernet"
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
              <div className="text-right mt-4">
                <Link
                  to={`/architecture?arch=${arch}`}
                  className="btn btn-primary px-4"
                >
                  proceed
                </Link>
              </div>
            </Route>
          </div>
        </div>
      </div>
    </Fragment>
  );
};

export default Model;
