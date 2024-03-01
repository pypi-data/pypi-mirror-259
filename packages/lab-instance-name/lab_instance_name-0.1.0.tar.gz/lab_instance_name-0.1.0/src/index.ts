import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { Widget } from '@lumino/widgets';
import { IStatusBar } from '@jupyterlab/statusbar';

import { requestAPI } from './handler';

// eslint-disable-next-line @typescript-eslint/naming-convention
interface ServerResponse {
  data: string;
}

/**
 * Initialization data for the lab_instance_name extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'lab_instance_name:plugin',
  description:
    'A JupyterLab extension for showing the lab instance name on the statusbar.',
  autoStart: true,
  optional: [IStatusBar],
  activate: async (app: JupyterFrontEnd, statusBar: IStatusBar | null) => {
    const serverResponse: ServerResponse = await requestAPI<any>('name');

    const labInstanceName: string = serverResponse.data ?? '';

    if (statusBar) {
      const statusWidget = new Widget();
      statusWidget.node.textContent = labInstanceName;
      statusWidget.addClass('jp-LabInstanceName');

      statusBar.registerStatusItem('labInstanceName', {
        item: statusWidget
      });
    }
  }
};

export default plugin;
