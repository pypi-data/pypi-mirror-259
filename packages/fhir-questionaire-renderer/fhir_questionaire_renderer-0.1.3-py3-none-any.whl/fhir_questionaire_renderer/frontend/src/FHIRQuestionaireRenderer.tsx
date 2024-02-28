import {
  StreamlitComponentBase,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib";
import { ReactNode } from "react";
import { SmartFormsRenderer, getResponse } from "@aehrc/smart-forms-renderer";

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class FHIRQuestionnaireRenderer extends StreamlitComponentBase {
  componentDidMount() {
    this.adjustFrameHeight();
  }
  
  componentDidUpdate() {
    this.adjustFrameHeight();
  }
  
  adjustFrameHeight() {
    const questionCount = this.props.args.questionaire.items.length;
    const questionHeight = 50; // Adjust this value based on your needs
    const totalHeight = questionCount * questionHeight;
    Streamlit.setFrameHeight(totalHeight);
  }
  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    const questionnaire = this.props.args["questionaire"];

    return (
      <div
        ref={(elem) => this.setState({ height: elem?.clientHeight })}
        style={{ height: "min-content" }}
      >
        <SmartFormsRenderer questionnaire={questionnaire} />
        <button
          onClick={() => {
            Streamlit.setComponentValue(getResponse());
            // Do something with the questionnaire response
          }}
        >
          Submit
        </button>
      </div>
    );
  };
}

export default withStreamlitConnection(FHIRQuestionnaireRenderer);
