# disable autoscroll
%%javascript
IPython.OutputArea.prototype._should_scroll = function(lines) {
    return false;
}

# show all output from a cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ignore all warnings
import warnings
warnings.filterwarnings('ignore')


# automatic reloading and inline plotting
%reload_ext autoreload
%autoreload 2
%matplotlib inline


# seeding
def seed_everything(seed=1234):
  random.seed(seed)
  os.environ['PYTHONHASHSEED'] = str(seed)
  np.random.seed(seed)
  torch.manual_seed(seed)
  torch.cuda.manual_seed(seed)
  torch.backends.cudnn.deterministic = True
  seed_everything()


# show progressbar
import pandas as pd
from tqdm import tqdm
tqdm.pandas()
#train["text"].progress_apply(lambda x: x.split()).values
