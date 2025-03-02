import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'SECRET_URL'; // e.g., https://your-project.supabase.co
const supabaseAnonKey = 'SECRET_KEY'; // From Settings > API

export const supabase = createClient(supabaseUrl, supabaseAnonKey);



