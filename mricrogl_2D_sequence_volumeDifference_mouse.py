import gl
import sys
import os
print(sys.version)
print(gl.version())
gl.resetdefaults()

help(gl)

# Load main image and overlay
mep_path = os.path.join('C:/', 'Users', 'Enzon', 'Documents', 'Projects', 'MEP', 'mep-scripts')
reference_path = os.path.join(mep_path, 'Data', 'Mouse', 'Reference')
analysis_path = os.path.join(mep_path, 'Data', 'Mouse', 'Analysis')
main_path = os.path.join(reference_path, 'average_template_50_reoriented.nii.gz')
overlay1_path = os.path.join(analysis_path, 'annotation_50_reoriented_pVal_inv_sig_volIncrease.nii.gz')
overlay2_path = os.path.join(analysis_path, 'annotation_50_reoriented_pVal_inv_sig_volDecrease.nii.gz')
gl.loadimage(main_path)
gl.overlayload(overlay1_path)
gl.overlayload(overlay2_path)
gl.opacity(1, 50)
gl.opacity(2, 50)
gl.minmax(1, 0, 3)
gl.minmax(2, 0, 3)
gl.colorname(1, '1red')
gl.colorname(2, '3blue')
output_dir_path = os.path.join(analysis_path, 'imageSequenceFolders', 'pVal_inv_sig_InDe')
if not os.path.exists(output_dir_path):
	os.mkdir(output_dir_path)

y_min = -13.15
y_max = 0
y_step = 0.05

y = y_min
count = 0
while y <= y_max:
	print(y)
	count = count + 1
	print(count)

	gl.orthoviewmm(0, y, -4)
	gl.view(2)
	gl.linewidth(0)
	gl.colorbarposition(0)

	filepath = os.path.join(output_dir_path, 'imagenew' + '_' + str(round(count)).rjust(3, '0')) + '_' + str(y)
	gl.savebmp(filepath)

	y = y + y_step
	


