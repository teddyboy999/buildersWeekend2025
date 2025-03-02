// CsvDownloader.jsx
import { useEffect } from 'react';
import { supabase } from './supabaseClient';
import { ResizableBox } from 'react-resizable';
import 'react-resizable/css/styles.css'; // Default styles for resize handles

const CsvDownloader = () => {
  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    const statusEl = document.getElementById('status');
    const errorEl = document.getElementById('error');
    const tableContainer = document.getElementById('tableContainer');

    statusEl.textContent = 'Loading data...';
    errorEl.textContent = '';
    tableContainer.innerHTML = '';

    try {
      const { data, error } = await supabase
        .from('predicted_restock_data')
        .select('*');

      if (error) throw new Error(error.message);

      if (!data || data.length === 0) {
        statusEl.textContent = 'No data found in the table.';
        return;
      }

      let tableHTML = '<table class="border-collapse border border-gray-400 w-full"><thead><tr>';
      const headers = Object.keys(data[0]);
      headers.forEach(header => {
        tableHTML += `<th class="border border-gray-300 p-2 bg-gray-100">${header}</th>`;
      });
      tableHTML += '</tr></thead><tbody>';

      data.forEach(row => {
        tableHTML += '<tr>';
        headers.forEach(header => {
          tableHTML += `<td class="border border-gray-300 p-2">${row[header] ?? ''}</td>`;
        });
        tableHTML += '</tr>';
      });

      tableHTML += '</tbody></table>';
      tableContainer.innerHTML = tableHTML;
      statusEl.textContent = `Loaded ${data.length} rows successfully.`;
    } catch (err) {
      errorEl.textContent = `Error: ${err.message}`;
      statusEl.textContent = 'Failed to load data.';
      console.error('Fetch error:', err);
    }
  }

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <button onClick={fetchData} className="mb-4 px-4 py-2 bg-blue-500 text-white rounded">
        Load Data
      </button>
      <p id="status" className="mb-4"></p>
      <p id="error" className="text-red-500 mb-4"></p>
      <ResizableBox
        width={800} // Initial width in pixels
        height={400} // Initial height in pixels
        minConstraints={[300, 200]} // Minimum size
        maxConstraints={[1200, 800]} // Maximum size
        className="border border-gray-400 rounded overflow-auto"
      >
        <div id="tableContainer"></div>
      </ResizableBox>
    </div>
  );
};

export default CsvDownloader;