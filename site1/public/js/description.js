frappe.ui.form.on('Sales Invoice', {
    validate: function(frm) {
        update_item_count(frm);
    }
});

frappe.ui.form.on('Sales Invoice Item', {
    item_code: function(frm) {
        update_item_count(frm);
    }
});

function update_item_count(frm) {
    let count = (frm.doc.items).length;
    frm.set_value('custom_description', count);
}
