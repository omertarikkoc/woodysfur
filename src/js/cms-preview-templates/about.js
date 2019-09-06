import React from "react";

import Jumbotron from "./components/jumbotron";


export default class ValuesPreview extends React.Component {
    render() {
        const { entry, widgetFor, getAsset } = this.props;

        let image = getAsset(entry.getIn(["data", "image"]));

        // Bit of a nasty hack to make relative paths work as expected as a background image here
        if (image && !image.fileObj) {
            image = window.parent.location.protocol + "//" + window.parent.location.host + image;
        }

        const entryValues = entry.getIn(["data", "values"]);
        const values = entryValues ? entryValues.toJS() : [];

        return <div>
            <Jumbotron image={image} title={entry.getIn(["data", "title"])} />
            <div className="bg-off-white pv4">
                <div className="mw7 center ph3 pt4">
                    {widgetFor("body")}
                </div>
            </div>
        </div>;
    }
}
